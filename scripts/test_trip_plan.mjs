import test from "node:test";
import assert from "node:assert/strict";
import {
  validatePlan,
  planText,
  emailDraft,
  MAX_MAILTO_LENGTH,
} from "../trip-plan.mjs";

const sample = () => ({
  tripDate: "2026-11-25",
  departureTime: "09:00",
  people: "Alex and Sam",
  startingPoint: "Trailhead",
  destination: "Day hike",
  route: "Marked trail out and back",
  expectedReturn: "2026-11-25T16:00",
  callDeadline: "2026-11-25T18:00",
  contactNumbers: "604-555-0100",
});
test("required details and date ordering are checked without inventing a buffer", () => {
  const data = sample();
  assert.deepEqual(validatePlan(data), {});
  assert.equal(
    validatePlan({ ...data, route: "  " }).route,
    "Complete this field.",
  );
  assert(
    validatePlan({ ...data, expectedReturn: "2026-11-25T08:00" })
      .expectedReturn,
  );
  assert(
    validatePlan({ ...data, callDeadline: "2026-11-25T15:00" }).callDeadline,
  );
  assert.deepEqual(
    validatePlan({ ...data, callDeadline: data.expectedReturn }),
    {},
  );
  assert.deepEqual(
    validatePlan({
      ...data,
      expectedReturn: "2026-11-26T01:00",
      callDeadline: "2026-11-26T02:00",
    }),
    {},
  );
});
test("impossible dates, times and turnaround order are rejected", () => {
  const data = sample();
  assert(validatePlan({ ...data, tripDate: "2026-02-30" }).tripDate);
  assert(validatePlan({ ...data, departureTime: "24:00" }).departureTime);
  assert(
    validatePlan({ ...data, expectedReturn: "2026-13-01T16:00" })
      .expectedReturn,
  );
  assert(validatePlan({ ...data, turnaround: "2026-11-25T08:30" }).turnaround);
  assert.deepEqual(
    validatePlan({ ...data, turnaround: "2026-11-25T13:00" }),
    {},
  );
});
test("preview contains every supplied detail literally and distinct return/calling times", () => {
  const data = {
    ...sample(),
    people: "Zoé & Jörg",
    route: "Out via A?\nReturn via B & C <route>",
    groupSize: "2 people / 1 dog",
    turnaround: "2026-11-25T13:00",
    vehicle: "Blue car",
    satellite: "Device contact",
    medical: "Private note",
    equipment: "First item\nSecond item",
  };
  const text = planText(data);
  assert(text.indexOf("CALL 9-1-1") < text.indexOf("Planned route:"));
  for (const value of [
    "Zoé & Jörg",
    "Out via A?\nReturn via B & C <route>",
    "Blue car",
    "Device contact",
    "Private note",
    "First item\nSecond item",
    "Expected return:\n25 Nov 2026 at 16:00",
    "CALL 9-1-1 IF WE HAVE NOT RETURNED OR CHECKED IN BY:\n25 Nov 2026 at 18:00",
  ])
    assert(text.includes(value), value);
  assert(
    text.endsWith(
      "This is not an official rescue site. In an emergency, call 9-1-1.",
    ),
  );
});
test("email draft round trips Unicode, reserved characters and line breaks", () => {
  const data = {
    ...sample(),
    people: "Zoé & Jörg",
    route: "A? & B # C + 50%",
    destination: "Lake\nBcc: other@example.com",
  };
  const result = emailDraft(data, "friend+trip@example.com");
  assert(result.uri.length <= MAX_MAILTO_LENGTH);
  const parsed = new URL(result.uri);
  assert.equal(decodeURIComponent(parsed.pathname), "friend+trip@example.com");
  assert.equal(
    parsed.searchParams.get("body"),
    planText(data).replace(/\n/g, "\r\n"),
  );
  assert(!parsed.searchParams.get("subject").includes("\n"));
  assert.deepEqual([...parsed.searchParams.keys()], ["subject", "body"]);
  assert(emailDraft(data, "friend@example.com\nBcc: other@example.com").error);
  assert(emailDraft(data, "one@example.com,two@example.com").error);
  assert(emailDraft(sample(), "").uri.startsWith("mailto:?"));
});
test("long text is preserved and uses copy fallback rather than a truncated email", () => {
  const data = { ...sample(), route: "Long route detail. ".repeat(110) };
  assert(planText(data).includes(data.route.trim()));
  assert(emailDraft(data).error.includes("Copy the complete text"));
  assert.equal(emailDraft(data).uri, undefined);
});

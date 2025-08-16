import { z } from "zod";
import { validateJson } from "../jsonValidator";

describe("validateJson", () => {
  it("should validate correct JSON", () => {
    const schema = z.object({ name: z.string(), age: z.number() });
    const data = { name: "Alice", age: 30 };
    expect(validateJson(schema, data)).toEqual(data);
  });

  it("should throw error for invalid JSON", () => {
    const schema = z.object({ name: z.string(), age: z.number() });
    const data = { name: "Bob", age: "not a number" };
    expect(() => validateJson(schema, data)).toThrow();
  });
});

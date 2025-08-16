// JSON型検証ユーティリティ
import { z } from "zod";

export function validateJson<T>(schema: z.ZodSchema<T>, data: unknown): T {
  const result = schema.safeParse(data);
  if (!result.success) {
    throw new Error("JSON validation failed: " + JSON.stringify(result.error.issues));
  }
  return result.data;
}

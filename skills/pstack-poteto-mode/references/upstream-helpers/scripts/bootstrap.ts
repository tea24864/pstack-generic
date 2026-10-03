import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";

export function ensureDependenciesInstalled(): void {
  const path = join(import.meta.dir, "node_modules", "commander", "package.json");
  if (!existsSync(path)) {
    throw new Error("Missing pre-existing commander 14.0.0. This port never auto-installs dependencies; obtain explicit setup approval or use direct gh reads.");
  }
  const installed = JSON.parse(readFileSync(path, "utf8"));
  if (installed.version !== "14.0.0") {
    throw new Error("Expected pre-existing commander 14.0.0; no automatic installation or fallback is allowed.");
  }
}

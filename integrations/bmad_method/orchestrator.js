/**
 * orchestrator.js
 * BMAD Orchestrator: parses BMAD configs and dispatches tasks to Warp/Unity MCP.
 */
import fs from "fs";
import yaml from "js-yaml";

export function loadTeams(configPath) {
  try {
    const file = fs.readFileSync(configPath, "utf8");
    return yaml.load(file);
  } catch (err) {
    console.error("Failed to load BMAD config:", err.message);
    return null;
  }
}

export function orchestrate(teamConfig) {
  if (!teamConfig) {
    console.error("No team config provided");
    return;
  }
  console.log("BMAD Orchestration started:", teamConfig);
  // TODO: Map roles → Unity MCP calls
}

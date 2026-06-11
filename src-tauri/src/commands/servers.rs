use std::path::PathBuf;

use serde::{Deserialize, Serialize};
use tauri::command;

#[derive(Debug, Deserialize, Serialize)]
pub struct Server {
    description: String,
    id: String,
    name: String,
    profile_url: String,
}

#[command]
pub async fn get_servers() -> Result<Vec<Server>, String> {
    // grab the list of messages
    let path = PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .join("test-data")
        .join("servers.json");

    let file = std::fs::read_to_string(path).map_err(|e| e.to_string())?;

    let servers: Vec<Server> =
        serde_json::from_str(&file).map_err(|e| format!("Failed to parse servers.json: {}", e))?;

    Ok(servers)
}

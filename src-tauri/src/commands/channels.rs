use std::path::PathBuf;

use serde::{Deserialize, Serialize};
use tauri::command;

#[derive(Debug, Deserialize, Serialize)]
pub struct Channel {
    description: String,
    id: String,
    name: String,
    server_id: String,
    pinned_messages: Vec<String>,
}

#[command]
pub async fn get_channels(server_id: String) -> Result<Vec<Channel>, String> {
    // grab the list of messages
    let path = PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .join("test-data")
        .join("channels.json");

    let file = std::fs::read_to_string(path).map_err(|e| e.to_string())?;

    let channels: Vec<Channel> =
        serde_json::from_str(&file).map_err(|e| format!("Failed to parse channels.json: {}", e))?;

    let filtered_channels: Vec<Channel> = channels
        .into_iter()
        .filter(|channel| channel.server_id == server_id)
        .collect();

    Ok(filtered_channels)
}

use std::path::PathBuf;

use serde::{Deserialize, Serialize};
use tauri::command;

#[derive(Debug, Deserialize, Serialize)]
struct Message {
    channel_id: u32,
    contents: String,
    id: u32,
    timestamp: u32,
    user_id: u32,
}

#[command]
pub async fn get_messages(channel_id: u32) -> Result<String, String> {
    // grab the list of messages
    let path = PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .join("test-data")
        .join("messages.json");

    let file = std::fs::read_to_string(path).map_err(|e| e.to_string())?;

    let messages: Vec<Message> =
        serde_json::from_str(&file).map_err(|e| format!("Failed to parse messages.json: {}", e))?;

    let filtered_messages: Vec<Message> = messages
        .into_iter()
        .filter(|message| message.channel_id == channel_id)
        .collect();

    serde_json::to_string(&filtered_messages).map_err(|e| e.to_string())
}

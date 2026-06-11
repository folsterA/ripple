use serde::{Deserialize, Serialize};
use tauri::command;

#[derive(Debug, Deserialize, Serialize)]
struct Server {
    description: String,
    id: String,
    name: String,
    profile_url: String,
}

#[command]
pub async fn get_servers() -> Result<String, String> {
    // grab the list of messages
    let path = format!(
        "{}/src-tauri/test-data/servers.json",
        env!("CARGO_MANIFEST_DIR")
    );
    let file = std::fs::read_to_string(path).map_err(|e| e.to_string())?;

    let servers: Vec<Server> =
        serde_json::from_str(&file).map_err(|e| format!("Failed to parse servers.json: {}", e))?;

    serde_json::to_string(&servers).map_err(|e| e.to_string())
}

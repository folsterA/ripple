use std::path::PathBuf;

use serde::{Deserialize, Serialize};
use tauri::command;

#[derive(Debug, Deserialize, Serialize)]
struct User {
    id: String,
    name: String,
    profile_url: String,
}

#[command]
pub async fn get_user(id: String) -> Result<String, String> {
    // grab the list of users
    let path = PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .join("test-data")
        .join("users.json");

    let file = std::fs::read_to_string(path).map_err(|e| e.to_string())?;

    // unwrap it into a list of users
    let users: Vec<User> =
        serde_json::from_str(&file).map_err(|e| format!("Failed to parse users.json: {}", e))?;

    // filter for the user id
    users
        .iter()
        .find(|user| user.id == id)
        .ok_or_else(|| format!("User with id {} not found", id))
        .and_then(|user| serde_json::to_string(user).map_err(|e| e.to_string()))
}

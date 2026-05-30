use tauri::command;

#[command]
pub async fn get_channels(_server_id: u32) -> Result<String, String> {
    Ok("Test".to_string())
}

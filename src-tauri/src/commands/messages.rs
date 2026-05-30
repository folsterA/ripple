use tauri::command;

#[command]
pub async fn get_messages(_channel_id: u32) -> Result<String, String> {
    Ok("Test".to_string())
}

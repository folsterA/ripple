use tauri::command;

#[command]
pub async fn get_user(id: u32) -> Result<String, String> {
    Ok(format!("User {}", id))
}

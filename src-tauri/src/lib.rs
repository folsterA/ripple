#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .setup(|app| {
            let app_handle = app.handle();
            if cfg!(debug_assertions) {
                app_handle.plugin(
                    tauri_plugin_log::Builder::default()
                        .level(log::LevelFilter::Info)
                        .build(),
                )?;

                let cwd = std::env::current_dir().expect("failed to get cwd");
                let script = cwd
                    .parent()
                    .expect("no parent directory")
                    .join("scripts/generate_test_data.py");

                std::process::Command::new("python")
                    .arg(script)
                    .status()
                    .expect("failed to generate test data");
            }

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}

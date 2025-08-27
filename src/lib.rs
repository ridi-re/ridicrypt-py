use pyo3::prelude::*;

mod decrypt;
mod global_key;
mod settings;

#[pymodule]
fn ridicrypt(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    let decrypt_mod = PyModule::new(_py, "decrypt")?;
    decrypt::register(&decrypt_mod)?;
    m.add_submodule(&decrypt_mod)?;

    let global_key_mod = PyModule::new(_py, "global_key")?;
    global_key::register(&global_key_mod)?;
    m.add_submodule(&global_key_mod)?;

    let settings_mod = PyModule::new(_py, "settings")?;
    settings::register(&settings_mod)?;
    m.add_submodule(&settings_mod)?;

    Ok(())
}

use pyo3::prelude::*;

mod decrypt;
mod settings;
mod utils;

mod py_utils;

#[pymodule]
fn ridicrypt(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    let decrypt_mod = PyModule::new(_py, "decrypt")?;
    decrypt::register(&decrypt_mod)?;
    m.add_submodule(&decrypt_mod)?;

    let settings_mod = PyModule::new(_py, "settings")?;
    settings::register(&settings_mod)?;
    m.add_submodule(&settings_mod)?;

    let utils_mod = PyModule::new(_py, "utils")?;
    utils::register(&utils_mod)?;
    m.add_submodule(&utils_mod)?;

    Ok(())
}

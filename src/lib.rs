use pyo3::prelude::*;

mod datastores;
mod decrypt;
mod utils;

mod py_utils;

#[pymodule]
fn ridicrypt(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    let decrypt_mod = PyModule::new(_py, "decrypt")?;
    decrypt::register(&decrypt_mod)?;
    m.add_submodule(&decrypt_mod)?;

    let datastores_mod = PyModule::new(_py, "datastores")?;
    datastores::register(&datastores_mod)?;
    m.add_submodule(&datastores_mod)?;

    let utils_mod = PyModule::new(_py, "utils")?;
    utils::register(&utils_mod)?;
    m.add_submodule(&utils_mod)?;

    Ok(())
}

use pyo3::prelude::*;
use ridicrypt_core::utils;

use crate::py_utils::IntoPyResult;

#[pyfunction]
pub fn get_global_key() -> PyResult<String> {
    utils::get_global_key().into_py()
}

#[pyfunction]
pub fn get_settings_path() -> PyResult<String> {
    utils::get_settings_path()
        .map(|p| p.to_string_lossy().into_owned())
        .into_py()
}

pub fn register(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_global_key, m)?)?;
    m.add_function(wrap_pyfunction!(get_settings_path, m)?)?;
    Ok(())
}

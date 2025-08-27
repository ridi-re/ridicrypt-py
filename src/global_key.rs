use pyo3::prelude::*;
use ridicrypt_core::global_key;

#[pyfunction]
pub fn get() -> PyResult<String> {
    global_key::get().map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))
}

pub fn register(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get, m)?)?;
    Ok(())
}

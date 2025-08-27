use pyo3::prelude::*;
use ridicrypt_core::decrypt;

#[pyfunction]
pub fn to_bytes(key: &[u8], path: &str) -> PyResult<Vec<u8>> {
    decrypt::to_u8(key.as_ref(), path)
        .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))
}

#[pyfunction]
pub fn to_str(key: &[u8], path: &str) -> PyResult<String> {
    decrypt::to_string(key.as_ref(), path)
        .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))
}

#[pyfunction]
pub fn zip_legacy(key: &[u8], path: &str, target: &str) -> PyResult<()> {
    decrypt::zip_legacy(key.as_ref(), path, target)
        .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))
}

#[pyfunction]
pub fn zip(key: &[u8], path: &str, target: &str) -> PyResult<()> {
    decrypt::zip(key.as_ref(), path, target)
        .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))
}

pub fn register(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(to_bytes, m)?)?;
    m.add_function(wrap_pyfunction!(to_str, m)?)?;
    m.add_function(wrap_pyfunction!(zip_legacy, m)?)?;
    m.add_function(wrap_pyfunction!(zip, m)?)?;
    Ok(())
}

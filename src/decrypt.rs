use pyo3::prelude::*;
use ridicrypt_core::decrypt;

use crate::py_utils::IntoPyResult;

#[pyfunction]
pub fn to_str(key: &str, path: &str) -> PyResult<String> {
    decrypt::to_string(key, path).into_py()
}

#[pyfunction]
pub fn binary(key: &str, path: &str, target: &str) -> PyResult<()> {
    decrypt::binary(key, path, target).into_py()
}

#[pyfunction]
pub fn zip(key: &str, path: &str, target: &str) -> PyResult<()> {
    decrypt::zip(key, path, target).into_py()
}

pub fn register(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(to_str, m)?)?;
    m.add_function(wrap_pyfunction!(binary, m)?)?;
    m.add_function(wrap_pyfunction!(zip, m)?)?;
    Ok(())
}

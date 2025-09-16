use pyo3::prelude::*;
use ridicrypt_core::datastores;

use crate::py_utils::IntoPyResult;

#[pyfunction]
pub fn decrypt(key: &str, path: &str) -> PyResult<String> {
    datastores::decrypt(key, path).into_py()
}

pub fn register(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(decrypt, m)?)?;
    Ok(())
}

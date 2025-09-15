use pyo3::PyResult;

pub trait IntoPyResult<T> {
    fn into_py(self) -> PyResult<T>;
}

impl<T> IntoPyResult<T> for Result<T, Box<dyn std::error::Error>> {
    fn into_py(self) -> PyResult<T> {
        self.map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))
    }
}

impl<T> IntoPyResult<T> for Option<T> {
    fn into_py(self) -> PyResult<T> {
        self.ok_or_else(|| pyo3::exceptions::PyRuntimeError::new_err("None value"))
    }
}

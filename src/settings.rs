use pyo3::prelude::*;
use ridicrypt_core::settings;

#[pyclass]
pub struct Settings {
    inner: settings::Settings,
}

#[pymethods]
impl Settings {
    #[getter]
    fn schema_version(&self) -> u32 {
        self.inner.schema_version
    }

    #[getter]
    fn data(&self) -> Data {
        Data {
            inner: self.inner.data.clone(),
        }
    }
}

#[pyclass]
pub struct Data {
    inner: settings::Data,
}

#[pymethods]
impl Data {
    #[getter]
    fn auto_login(&self) -> AutoLogin {
        AutoLogin {
            inner: self.inner.auto_login.clone(),
        }
    }

    #[getter]
    fn device(&self) -> Device {
        Device {
            inner: self.inner.device.clone(),
        }
    }
}

#[pyclass]
pub struct AutoLogin {
    inner: settings::AutoLogin,
}

#[pymethods]
impl AutoLogin {
    #[getter]
    fn username(&self) -> &str {
        &self.inner.username
    }
    #[getter]
    fn refresh_token(&self) -> &str {
        &self.inner.refresh_token
    }
}

#[pyclass]
pub struct Device {
    inner: settings::Device,
}

#[pymethods]
impl Device {
    #[getter]
    fn device_id(&self) -> &str {
        &self.inner.device_id
    }
    #[getter]
    fn device_nick(&self) -> &str {
        &self.inner.device_nick
    }
}

#[pyfunction]
pub fn decrypt(key: &str) -> PyResult<Settings> {
    settings::decrypt(key)
        .map(|s| Settings { inner: s })
        .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))
}

pub fn register(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Settings>()?;
    m.add_class::<Data>()?;
    m.add_class::<AutoLogin>()?;
    m.add_class::<Device>()?;
    m.add_function(wrap_pyfunction!(decrypt, m)?)?;
    Ok(())
}

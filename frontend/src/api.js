import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000', // URL de tu backend FastAPI
  headers: {
    'Content-Type': 'application/json',
  }
});

// Interceptor para agregar el token de autorización a las solicitudes
apiClient.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default {
  getReservas() {
    return apiClient.get('/reservas/');
  },
  createReserva(reserva) {
    return apiClient.post('/reservas/', reserva);
  },
  getAdministradores() {
    return apiClient.get('/administradores/');
  },
  createAdministrador(admin) {
    return apiClient.post('/administradores/', admin);
  },
  deleteAdministrador(id) {
    return apiClient.delete(`/administradores/${id}`);
  },
  getSocios() {
    return apiClient.get('/socios/');
  },
  createSocio(socio) {
    return apiClient.post('/socios/', socio);
  },
  deleteSocio(id) {
    return apiClient.delete(`/socios/${id}`);
  },
  getPistas() {
    return apiClient.get('/pistas/');
  },
  createPista(pista) {
    return apiClient.post('/pistas/', pista);
  },
  deletePista(id) {
    return apiClient.delete(`/pistas/${id}`);
  },
  // Agrega más métodos según sea necesario
};
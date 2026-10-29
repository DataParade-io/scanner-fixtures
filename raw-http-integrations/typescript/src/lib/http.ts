// One shared axios instance for the whole app; other modules import it.
import axios from "axios";

export const backend = axios.create({ baseURL: import.meta.env.VITE_BACKEND_URL });

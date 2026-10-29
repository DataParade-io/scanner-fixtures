// The base URL exists only in build-time configuration, so the destination is unknown.
import axios from "axios";

const orders = axios.create({ baseURL: import.meta.env.VITE_ORDERS_API_URL });

export async function placeOrder(cartId: string, shippingAddress: string) {
  const { data } = await orders.post("/orders", { cartId, shippingAddress });
  return data;
}

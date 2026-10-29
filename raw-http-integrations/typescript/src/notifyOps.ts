// Posts to a webhook whose URL is defined in another module.
import { ALERTS_WEBHOOK_URL } from "./settings";

export async function notifyOps(orderId: string, customerEmail: string) {
  await fetch(ALERTS_WEBHOOK_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: `Refund requested for order ${orderId} by ${customerEmail}` }),
  });
}

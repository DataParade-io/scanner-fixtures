// An axios instance carries the base URL; calls use relative paths.
import axios from "axios";

const crm = axios.create({
  baseURL: "https://api.hubapi.com",
  headers: { Authorization: `Bearer ${process.env.HUBSPOT_TOKEN}` },
});

export async function upsertContact(email: string, firstName: string, phone: string) {
  await crm.post("/crm/v3/objects/contacts", {
    properties: { email, firstname: firstName, phone },
  });
}

// The API base is a module constant that callers may override; axios gets a template literal.
import axios from "axios";

const DEFAULT_API_BASE = "https://api.airtable.com/v0";

export async function saveSignup(
  email: string,
  fullName: string,
  apiBase: string = DEFAULT_API_BASE,
): Promise<string> {
  const { data } = await axios.post(
    `${apiBase}/${process.env.AIRTABLE_BASE_ID}/Signups`,
    { fields: { Email: email, Name: fullName } },
    { headers: { Authorization: `Bearer ${process.env.AIRTABLE_TOKEN}` } },
  );
  return data.id;
}

// The default API base is the team's own service on Google Cloud Run.
import axios from "axios";

const DEFAULT_AGENT_API = "https://shop-agent-482913.europe-west1.run.app";

export async function sendToAgent(message: string, sessionId: string, apiBase = DEFAULT_AGENT_API) {
  const { data } = await axios.post(`${apiBase}/agent/chat`, { message, sessionId });
  return data.reply as string;
}

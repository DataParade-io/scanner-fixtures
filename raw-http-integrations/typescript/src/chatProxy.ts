// Express route that forwards a visitor's chat to a hosted model with fetch.
import type { Request, Response } from "express";

export async function chatProxy(req: Request, res: Response) {
  const { messages, visitorId } = req.body;
  const upstream = await fetch("https://api.mistral.ai/v1/chat/completions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${process.env.MISTRAL_API_KEY}`,
    },
    body: JSON.stringify({ model: "mistral-small-latest", messages, user: visitorId }),
  });
  res.status(upstream.status).json(await upstream.json());
}

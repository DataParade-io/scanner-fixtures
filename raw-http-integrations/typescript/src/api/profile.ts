// Uses the shared instance from lib/http; the base URL comes only from env.
import { backend } from "../lib/http";

export async function updateProfile(userId: string, displayName: string, phone: string) {
  await backend.patch(`/users/${userId}`, { displayName, phone });
}

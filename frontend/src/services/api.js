export async function getEmails() {
  const response = await fetch("http://localhost:8000/emails");
  return response.json();
}

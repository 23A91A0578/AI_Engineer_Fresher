import React, { useState, useEffect } from "react";
import EmailList from "../components/EmailList";
import EmailDetail from "../components/EmailDetail";
import Analytics from "../components/Analytics";
import { getEmails } from "../services/api";

const Dashboard = () => {
  const [emails, setEmails] = useState([]);
  const [selectedEmail, setSelectedEmail] = useState(null);

  useEffect(() => {
    getEmails().then(data => setEmails(data));
  }, []);

  return (
    <div style={{ display: "flex" }}>
      <EmailList emails={emails} onSelect={setSelectedEmail} />
      {selectedEmail && <EmailDetail email={selectedEmail} />}
      <Analytics emails={emails} />
    </div>
  );
};

export default Dashboard;

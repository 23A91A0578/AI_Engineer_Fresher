import React from "react";

const EmailList = ({ emails, onSelect }) => (
  <div style={{ width: "30%", borderRight: "1px solid gray" }}>
    <h2>Emails</h2>
    <ul>
      {emails.map(email => (
        <li key={email.id} onClick={() => onSelect(email)}>
          <b>{email.subject}</b> ({email.priority})
        </li>
      ))}
    </ul>
  </div>
);

export default EmailList;

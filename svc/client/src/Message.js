export const Message = ({ message }) => {
  // if (message.type === 'join') return <p>{`${message.sid} just joined`}</p>;
  return <p>{`${message.sender.first_name} ${message.sender.last_name}: ${message.text}`}</p>;
};

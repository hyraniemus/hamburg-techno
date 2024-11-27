export function addDays(date: Date, days: number): Date {
  const result = new Date(date);
  result.setDate(result.getDate() + days);
  return result;
}

export function getToday(): Date {
  const today = new Date();
  today.setHours(22, 0, 0, 0); // Set to 22:00 for events
  return today;
}

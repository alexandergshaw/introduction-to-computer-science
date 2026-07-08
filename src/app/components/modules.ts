export type ModuleType = "assignment" | "review" | "exam";

export type ModuleDefinition = {
  slug: string;
  week: number;
  title: string;
  type: ModuleType;
};

export const moduleDefinitions: ModuleDefinition[] = [
  { slug: "week-00-assignment", week: 0, title: "Orientation", type: "assignment" },
  { slug: "week-01-assignment", week: 1, title: "Python Basics", type: "assignment" },
  { slug: "week-02-assignment", week: 2, title: "Variables and Deployment", type: "assignment" },
  { slug: "week-03-assignment", week: 3, title: "Logic and Control Flow", type: "assignment" },
  { slug: "week-04-assignment", week: 4, title: "Functions and Modular Programming", type: "assignment" },
  { slug: "week-05-assignment", week: 5, title: "Data Structures", type: "assignment" },
  { slug: "week-06-review", week: 6, title: "Review 1", type: "review" },
  { slug: "week-07-exam", week: 7, title: "Exam 1", type: "exam" },
  { slug: "week-08-assignment", week: 8, title: "OOP Classes", type: "assignment" },
  { slug: "week-09-assignment", week: 9, title: "Advanced OOP", type: "assignment" },
  { slug: "week-10-assignment", week: 10, title: "Error Handling and File IO", type: "assignment" },
  { slug: "week-11-assignment", week: 11, title: "Unit Testing", type: "assignment" },
  { slug: "week-12-assignment", week: 12, title: "Advanced Unit Testing", type: "assignment" },
  { slug: "week-13-assignment", week: 13, title: "Best Practices", type: "assignment" },
  { slug: "week-14-review", week: 14, title: "Review 2", type: "review" },
  { slug: "week-15-exam", week: 15, title: "Exam 2", type: "exam" },
];

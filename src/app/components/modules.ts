export type ModuleType = "assignment" | "review" | "exam";

export type ModuleDefinition = {
  slug: string;
  week: number;
  title: string;
  type: ModuleType;
};

export const moduleDefinitions: ModuleDefinition[] = [
  { slug: "assignment0", week: 0, title: "Orientation", type: "assignment" },
  { slug: "assignment1", week: 1, title: "Environment Setup", type: "assignment" },
  { slug: "assignment2", week: 2, title: "Variables and Deployment", type: "assignment" },
  { slug: "assignment3", week: 3, title: "Logic and Control Flow", type: "assignment" },
  { slug: "assignment4", week: 4, title: "Functions and Modular Programming", type: "assignment" },
  { slug: "assignment5", week: 5, title: "Data Structures", type: "assignment" },
  { slug: "review6", week: 6, title: "Review 1", type: "review" },
  { slug: "assignment6", week: 6, title: "Supplemental Practice", type: "assignment" },
  { slug: "exam7", week: 7, title: "Exam Practice 1", type: "exam" },
  { slug: "assignment7", week: 7, title: "Supplemental Practice", type: "assignment" },
  { slug: "assignment8", week: 8, title: "OOP Classes", type: "assignment" },
  { slug: "assignment9", week: 9, title: "Advanced OOP", type: "assignment" },
  { slug: "assignment10", week: 10, title: "Error Handling and File IO", type: "assignment" },
  { slug: "assignment11", week: 11, title: "Unit Testing", type: "assignment" },
  { slug: "assignment12", week: 12, title: "Git and Branching", type: "assignment" },
  { slug: "assignment13", week: 13, title: "Best Practices", type: "assignment" },
  { slug: "review14", week: 14, title: "Review 2", type: "review" },
  { slug: "assignment14", week: 14, title: "Supplemental Practice", type: "assignment" },
  { slug: "exam15", week: 15, title: "Exam Practice 2", type: "exam" },
  { slug: "assignment15", week: 15, title: "Supplemental Practice", type: "assignment" },
  { slug: "assignment16", week: 16, title: "Final Project", type: "assignment" },
];

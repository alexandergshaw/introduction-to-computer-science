import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Introduction to Computer Science Dashboard",
  description: "Student portfolio dashboard for semester assignments and progress tracking.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="h-full antialiased">
      <body className="min-h-full text-slate-100">{children}</body>
    </html>
  );
}

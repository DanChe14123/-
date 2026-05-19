import "../styles.css";

export const metadata = {
  title: "实验室安全值班 | 在线游玩",
  description: "实验室安全值班 v2.0 在线协作桌游原型",
  icons: {
    icon: "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23007f79'/%3E%3Cpath d='M25 10h14v5l-3 4v12l13 19H15l13-19V19l-3-4z' fill='none' stroke='white' stroke-width='4' stroke-linejoin='round'/%3E%3Cpath d='M23 43h18' stroke='white' stroke-width='4' stroke-linecap='round'/%3E%3C/svg%3E",
  },
};

export default function RootLayout({ children }) {
  return (
    <html lang="zh-CN">
      <body>{children}</body>
    </html>
  );
}

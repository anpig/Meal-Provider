FROM node:18-alpine as builder

WORKDIR /app

RUN npm install -g pnpm@9.0.6

COPY package*.json ./
RUN pnpm install

COPY . .
RUN pnpm run build

FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]

// GraphQLクライアントユーティリティ
import axios, { AxiosInstance } from "axios";

export class GraphQLClient {
  private client: AxiosInstance;
  constructor(endpoint: string, headers: Record<string, string> = {}) {
    this.client = axios.create({ baseURL: endpoint, headers });
  }
  async query(query: string, variables: Record<string, any> = {}): Promise<any> {
    const response = await this.client.post("", { query, variables });
    if (response.data.errors) {
      throw new Error("GraphQL Error: " + JSON.stringify(response.data.errors));
    }
    return response.data.data;
  }
}

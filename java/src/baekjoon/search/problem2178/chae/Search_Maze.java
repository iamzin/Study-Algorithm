package baekjoon.search.problem2178.chae;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Search_Maze {
    /*
     * <BOJ - 2178 미로탐색> bfs로 탐색하면서 이전 좌표 값을 다음 좌표값에 더하고 visited의 해당 좌표 값 1로 바꿈
     * 마지막으로 (N,M)의 좌표 값을 가져오면 됨
     */

    static int[][] arr;
    static int[][] visited;

    public static void main(String[] args) throws IOException {
        Search_Maze S = new Search_Maze();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        arr = new int[n + 1][m + 1];
        visited = new int[n + 1][m + 1];

        for (int i = 1; i <= n; i++) {
            String input = br.readLine();
            for (int j = 1; j <= m; j++) {
                arr[i][j] = input.charAt(j - 1) - '0';
            }
        }

        System.out.println(S.bfs(n, m));
    }

    public class Coord {
        int row;
        int column;

        public Coord(int row, int column) {
            this.row = row;
            this.column = column;
        }
    }

    public int bfs(int n, int m) {
        // 큐에 담을 값: 인접 좌표(i,j)
        Queue<Coord> q = new LinkedList<>();
        q.add(new Coord(1, 1));
        visited[1][1] = 1;

        while (!q.isEmpty()) {
            Coord cur_coord = q.poll();
            ArrayList<Coord> coords = searchNextCoord(cur_coord, n, m);
            for (Coord coord : coords) {
                q.add(coord);
                visited[coord.row][coord.column] = visited[cur_coord.row][cur_coord.column] + 1;
            }
        }
        return visited[n][m];
    }

    public ArrayList<Coord> searchNextCoord(Coord coord, int n, int m) {
        ArrayList<Coord> nextNodeList = new ArrayList<>();
        int[] dx = { 0, 0, -1, 1 };
        int[] dy = { 1, -1, 0, 0 };

        int cur_row = coord.row;
        int cur_column = coord.column;

        for (int i = 0; i < 4; i++) {
            if (0 >= dx[i] + cur_column || dx[i] + cur_column > m || 0 >= dy[i] + cur_row || dy[i] + cur_row > n)
                continue;
            if (visited[dy[i] + cur_row][dx[i] + cur_column] != 0 || arr[dy[i] + cur_row][dx[i] + cur_column] == 0)
                continue;

            nextNodeList.add(new Coord(dy[i] + cur_row, dx[i] + cur_column));
        }
        return nextNodeList;
    }
}
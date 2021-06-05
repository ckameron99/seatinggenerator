public class algorithm{
@Override
    public Map<Integer, Map<Integer, Double>> getEdgeBetweenness(Map<Integer, Set<Integer>> graph) {
        Queue<Integer> queue = new LinkedList<>();
        Stack<Integer> stack = new Stack<>();

        Map<Integer, Map<Integer, Double>> betweenness = new HashMap<>();
        for (Map.Entry<Integer, Set<Integer>> entry : graph.entrySet()){
            betweenness.put(entry.getKey(), new HashMap<>());

            for (int w : entry.getValue()){
                betweenness.get(entry.getKey()).put(w, 0.0);
            }
        }

        Map<Integer, Double> delta = new HashMap<>();

        for (int s : graph.keySet()){
            Map<Integer, Integer> sigma = new HashMap<>();
            Map<Integer, Integer> distance = new HashMap<>();
            Map<Integer, List<Integer>> pred = new HashMap<>();

            for (int v : graph.keySet()){
                delta.put(v, 0.0);
                distance.put(v, -1);
                sigma.put(v, 0);
                pred.put(v, new ArrayList<>());
            }

            distance.put(s, 0);
            sigma.put(s, 1);
            queue.add(s);

            while (!queue.isEmpty()) {
                int v = queue.poll();
                stack.push(v);
                for (int w : graph.get(v)) {
                    if (distance.get(w) == -1){
                        distance.put(w, distance.get(v) + 1);
                        queue.add(w);
                    }
                    if (distance.get(w) == distance.get(v) + 1){
                        sigma.put(w, sigma.get(w) + sigma.get(v));
                        pred.get(w).add(v);
                    }
                }
            }

            while (!stack.isEmpty()){
                int w = stack.pop();
                for (int v : pred.get(w)){
                    double c = ((double) sigma.get(v) / sigma.get(w)) * (1.0 + delta.get(w));
                    betweenness.get(v).put(w, betweenness.get(v).get(w) + c);
                    delta.put(v,delta.get(v) + c);
                }
            }
        }

        return betweenness;
    }
}
}
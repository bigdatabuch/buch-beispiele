package com.example;

import org.apache.flink.api.common.typeinfo.Types;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.util.Collector;
import org.apache.flink.util.ParameterTool;

public class SocketWordCount {

  public static void main(String[] args) throws Exception {
    final ParameterTool params = ParameterTool.fromArgs(args);
    final String host = params.get("host", "textsource");
    final int port = params.getInt("port", 9000);

    final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

    DataStream<String> lines = env.socketTextStream(host, port, "\n"); // für Demos ok

    DataStream<Tuple2<String, Integer>> counts =
        lines
          .flatMap((String line, Collector<Tuple2<String, Integer>> out) -> {
            for (String token : line.toLowerCase().split("\\W+")) {
              if (!token.isEmpty()) out.collect(Tuple2.of(token, 1));
            }
          })
          .returns(Types.TUPLE(Types.STRING, Types.INT))
          .keyBy(t -> t.f0)
          .sum(1)
          .name("wordcount");

    counts.print().name("print");
    env.execute("Socket WordCount (Flink 2.1)");
  }
}

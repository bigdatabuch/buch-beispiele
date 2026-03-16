package de.hsma.bdea;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.log4j.BasicConfigurator;

public class CardCount {

	public static class TokenizerMapper extends Mapper<Object, Text, Text, IntWritable> {
		private final static IntWritable one = new IntWritable(1);
		private Text color = new Text();

		// für jede Zeile der Input-Dateien wird einmal die Map-Methode aufgerufen
		public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
			String[] spalten = value.toString().split(",");
			color.set(spalten[1]);
			context.write(color, one);  // return
		}
	}

	// zur Illustration, wie der Reduce funktioniert
	// Hadoop liefert einen IntSumReducer bereits fertig mit
	// -> import org.apache.hadoop.mapreduce.lib.reduce.IntSumReducer; macht diese Klasse überflüssig
	public static class IntSumReducer extends Reducer<Text,IntWritable,Text,IntWritable> {
		private IntWritable result = new IntWritable();

		public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
			int sum = 0;
			for (IntWritable val : values) {
				sum += val.get();
			}
			result.set(sum);
			context.write(key, result);
		}
	}

	public static void main(String[] args) throws Exception {
		BasicConfigurator.configure(); 					// Log4j Config oder ConfigFile in Resources Folder
		System.setProperty("hadoop.home.dir", "/");  	// zwingend für Hadoop 3.3.0

		Configuration conf = new Configuration();

		Job job = Job.getInstance(conf, "card count");
		job.setJarByClass(CardCount.class);
		job.setMapperClass(TokenizerMapper.class);
		job.setCombinerClass(IntSumReducer.class);	// "pre-reduce" lokal bei den Mappern
		job.setReducerClass(IntSumReducer.class);	// reduce nach Verteilung auf die Reducern
		job.setNumReduceTasks(2);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		
		FileInputFormat.addInputPath(job, new Path("src/test/resources/karten*.csv"));	// * als Wildcard verwendet
		FileOutputFormat.setOutputPath(job, new Path("/tmp/karten-output" + System.currentTimeMillis()));

		System.exit(job.waitForCompletion(true) ? 0 : 1);
	}
}

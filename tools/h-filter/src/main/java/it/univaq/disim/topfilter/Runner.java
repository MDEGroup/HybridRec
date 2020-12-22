package it.univaq.disim.topfilter;


import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.Properties;

import org.apache.log4j.Logger;

import it.univaq.disim.topfilter.validation.Validator;





public class Runner {
	
	private String srcDir;	
	private String subFolder;
	private int numOfProjects;
	private static final int numOfNeighbours = 20;
	private static String _propFile = "evaluation.properties";
	final static Logger logger = Logger.getLogger(Runner.class);
	public Runner(){
		
	}
	
	public String loadConfigurations() throws FileNotFoundException, IOException{		
		Properties prop = new Properties();				
		prop.load(getClass().getClassLoader().getResourceAsStream(_propFile));		
		return prop.getProperty("sourceDirectory");
	}
	
	public void run(boolean bayesian) throws FileNotFoundException, IOException{
		
		logger.info("TopFilter: Recommender System!");
		
		String srcDir = loadConfigurations();
		this.srcDir = srcDir;
		DataReader dr = new DataReader(srcDir);
		numOfProjects = dr.getNumberOfProjects(Paths.get(this.srcDir, "projects.txt").toString());		
		tenFoldCrossValidation(bayesian);
		logger.info(System.currentTimeMillis());		
		Validator validator = new Validator(srcDir, bayesian);
		validator.run();
		logger.info("Neighbor:" + numOfNeighbours);
		logger.info("Dataset:" + this.srcDir);
	}
	public void tenFoldCrossValidation(boolean bayesian) {
		int step = (int)numOfProjects/10;								
							
		for(int i=0;i<10;i++) {
			
			int trainingStartPos1 = 1;			
			int trainingEndPos1 = i*step;			
			int trainingStartPos2 = (i+1)*step+1;
			int trainingEndPos2 = numOfProjects;
			int testingStartPos = 1+i*step;
			int testingEndPos =   (i+1)*step;
			
			int k=i+1;
			subFolder = "Round" + Integer.toString(k);			
	
			logger.info("Computing similarities fold " + i);
			//TODO CHANGE HERE
			
			TopicSimilarityCalculator calculator = new TopicSimilarityCalculator(this.srcDir,this.subFolder,
					trainingStartPos1,
					trainingEndPos1,
					trainingStartPos2,
					trainingEndPos2,
					testingStartPos,
					testingEndPos,
					bayesian);
			
			calculator.computeWeightCosineSimilarity();
			logger.info("\tComputed similarities fold " + i);
			logger.info("Computing recommendations fold " + i);
			RecommendationEngine engine = new RecommendationEngine(this.srcDir,this.subFolder,numOfNeighbours,testingStartPos,testingEndPos, bayesian);
//NOT FOR THIS PAPER		    engine.ItemBasedRecommendation();					   		    
			engine.userBasedRecommendation();	
			logger.info("\tComputed recommendations fold " + i);
		}
		
	}
	
	public static void main(String[] args) {	
		Runner runner = new Runner();			
		try {
			runner.run(true);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}				    		    
		return;
	}	
	
}

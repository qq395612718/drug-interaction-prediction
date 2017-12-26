package jenatuili;

/**
 * @purpose Object creation factory
 * 
 * 
 */
public class ReasonerFactory {

	public static IReasoner createFamilyReasoner() {
		IReasoner familyReasoner = new Reasonerlmpl();
		return familyReasoner;
	}
}


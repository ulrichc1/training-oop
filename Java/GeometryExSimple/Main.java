public class Main {
    public static void main(String[] args){
        Cercle cercleR = new Cercle(10,"Cercle Rouge","red");
        Cercle cercleB = new Cercle(5,"Cercle Bleu", "blue");
        Rectangle rectangleR = new Rectangle(10,20,"Rectangle rouge","red");
        Rectangle rectangleB = new Rectangle(5,15,"Rectangle bleu", "bleu");

        // Affichage basique
        System.out.println(cercleR.getCouleur());
        System.out.println(cercleB.getCouleur());
        System.out.println(rectangleR.getCouleur());
        System.out.println(rectangleB.getCouleur());
        System.out.println(cercleR.toString());
        System.out.println(cercleB.toString());
        System.out.println(rectangleR.toString());
        System.out.println(rectangleB.toString());

        // Mesures, Aires & Périmètres
        System.out.println(cercleR.getRayon());
        System.out.println(cercleB.getRayon());
        System.out.println(rectangleR.getLongueur() + " " + rectangleR.getLargeur());
        System.out.println(rectangleB.getLongueur() + " " + rectangleB.getLargeur());

        System.out.println(cercleR.calculerAire());
        System.out.println(cercleB.calculerAire());
        System.out.println(rectangleR.calculerAire());
        System.out.println(rectangleB.calculerAire());



    }
}

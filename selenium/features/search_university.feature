Feature: Buscar universidades y contenido académico

  Scenario Outline: Buscar universidad y diferentes contenidos
    Given I open Google
    When I search for "<universidad>"
    And I click on the first result
    Then I should be on "<dominio>"
    When I search inside the site for "<busqueda>"
    Then I should see results related to "<busqueda>"

    Examples:
      | universidad | dominio   | busqueda        |
      | iteso       | iteso.mx  | carreras        |
      | iteso       | iteso.mx  | admisiones      |
      | iteso       | iteso.mx  | posgrados       |
      | udg         | udg.mx    | carreras        |
      | udg         | udg.mx    | admision        |
      | udg         | udg.mx    | investigación   |
      | unam        | unam.mx   | licenciaturas   |
      | unam        | unam.mx   | posgrado        |
      | unam        | unam.mx   | convocatoria    |
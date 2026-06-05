cube(`CampusEvents`, {
  sql: `SELECT * FROM campus_events`,

  measures: {
    eventsCount: {
      type: `count`,
      title: `EventsCount`
    },

    activeStudents: {
      sql: `student_id`,
      type: `countDistinct`,
      title: `ActiveStudents`
    },

    roomEntries: {
      type: `count`,
      filters: [{ sql: `${CUBE}.event_type = 'student_entered_campus'` }],
      title: `RoomEntries`
    },

    roomExits: {
      type: `count`,
      filters: [{ sql: `${CUBE}.event_type = 'student_left_campus'` }],
      title: `RoomExits`
    }
  },

  dimensions: {
    eventId: {
      sql: `event_id`,
      type: `string`,
      primaryKey: true
    },

    studentId: {
      sql: `student_id`,
      type: `number`
    },

    eventType: {
      sql: `event_type`,
      type: `string`
    },

    building: {
      sql: `building`,
      type: `string`
    },

    room: {
      sql: `room`,
      type: `string`
    },

    eventTime: {
      sql: `event_time`,
      type: `time`
    }
  }
});
